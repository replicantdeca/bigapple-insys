# from __future__ import print_function
from plotly import __version__

# Import Python wrapper for or-tools constraint solver.
from ortools.constraint_solver import pywrapcp
from plotly.offline import plot
import plotly.figure_factory as ff

'''
Job Shop example from 
https://developers.google.com/optimization/scheduling/job_shop
with gantt chart
'''


# FIXME: create_gantt requires dates or times
def draw_gantt_chart_div(df):
    # Task     = Machine #
    # Resource = Job #
    # Start    = Time Interval X
    # Finish   = Time Interval Y
    fig = ff.create_gantt(df, index_col='Resource', show_colorbar=True, group_tasks=True)
    gantt_chart_div = plot(fig, output_type='div')
    return gantt_chart_div


# FIXME: solve_jobshop should not call generate_gantt_chart_div inside itself(?)
def solve_jobshop():
    # Create the solver.
    solver = pywrapcp.Solver('jobshop')

    machines_count = 3
    jobs_count = 3
    all_machines = range(0, machines_count)
    all_jobs = range(0, jobs_count)
    # Define data.
    machines = [[0, 1, 2],
                [0, 2, 1],
                [1, 2]]

    processing_times = [[3, 2, 2],
                        [2, 1, 4],
                        [4, 3]]
    # Computes horizon.
    horizon = 0
    for i in all_jobs:
        horizon += sum(processing_times[i])
    # Creates jobs.
    all_tasks = {}
    for i in all_jobs:
        for j in range(0, len(machines[i])):
            all_tasks[(i, j)] = solver.FixedDurationIntervalVar(0,
                                                                horizon,
                                                                processing_times[i][j],
                                                                False,
                                                                'Job %i_%i' % (i, j))

    # Creates sequence variables and add disjunctive constraints.
    all_sequences = []
    for i in all_machines:

        machines_jobs = []
        for j in all_jobs:
            for k in range(0, len(machines[j])):
                if machines[j][k] == i:
                    machines_jobs.append(all_tasks[(j, k)])
        disj = solver.DisjunctiveConstraint(machines_jobs, 'machine %i' % i)
        all_sequences.append(disj.SequenceVar())
        solver.Add(disj)

    # Add conjunctive constraints.
    for i in all_jobs:
        for j in range(0, len(machines[i]) - 1):
            solver.Add(all_tasks[(i, j + 1)].StartsAfterEnd(all_tasks[(i, j)]))

    # Set the objective.
    obj_var = solver.Max([all_tasks[(i, len(machines[i])-1)].EndExpr()
                          for i in all_jobs])
    objective_monitor = solver.Minimize(obj_var, 1)
    # Create search phases.
    sequence_phase = solver.Phase([all_sequences[i] for i in all_machines],
                                  solver.SEQUENCE_DEFAULT)
    vars_phase = solver.Phase([obj_var],
                              solver.CHOOSE_FIRST_UNBOUND,
                              solver.ASSIGN_MIN_VALUE)
    main_phase = solver.Compose([sequence_phase, vars_phase])
    # Create the solution collector.
    collector = solver.LastSolutionCollector()

    # Add the interesting variables to the SolutionCollector.
    collector.Add(all_sequences)
    collector.AddObjective(obj_var)

    for i in all_machines:
        sequence = all_sequences[i];
        sequence_count = sequence.Size();
        for j in range(0, sequence_count):
            t = sequence.Interval(j)
            collector.Add(t.StartExpr().Var())
            collector.Add(t.EndExpr().Var())

    # Solve the problem.
    df = []
    task_list = []
    start_list = []
    finish_list = []
    resource_list = []
    disp_col_width = 10
    if solver.Solve(main_phase, [objective_monitor, collector]):
        # print("\nOptimal Schedule Length:", collector.ObjectiveValue(0), "\n")
        sol_line = ""
        sol_line_tasks = ""
        # print("Optimal Schedule", "\n")

        for i in all_machines:
            seq = all_sequences[i]
            sol_line += "Machine " + str(i) + ": "
            sol_line_tasks += "Machine " + str(i) + ": "
            task_list.append("Machine " + str(i))  # Machine number
            sequence = collector.ForwardSequence(0, seq)
            seq_size = len(sequence)

            for j in range(0, seq_size):
                t = seq.Interval(sequence[j]);
                # Add spaces to output to align columns.
                sol_line_tasks += t.Name() + " " * (disp_col_width - len(t.Name()))
                temp_name = t.Name().split('_', 1)[0]
                resource_list.append(temp_name)  # Job number

            for j in range(0, seq_size):
                t = seq.Interval(sequence[j]);
                sol_tmp = "[" + str(collector.Value(0, t.StartExpr().Var())) + ","
                sol_tmp += str(collector.Value(0, t.EndExpr().Var())) + "] "
                # FIXME: PLOTLY NEEDS START AND END AS TIME
                start_list.append(str(collector.Value(0, t.StartExpr().Var()) + 2000))  # Start Time must be string!
                finish_list.append(str(collector.Value(0, t.EndExpr().Var()) + 2000))  # Finish Time

                # Add spaces to output to align columns.
                sol_line += sol_tmp + " " * (disp_col_width - len(sol_tmp))

            for j in range(0, seq_size):
                temp_dict = {'Task': task_list[i],
                             'Start': start_list.pop(0),
                             'Finish': finish_list.pop(0),
                             'Resource': resource_list.pop(0)}
                # temp_dict['Task'] = task_list[i]
                # temp_dict['Start'] = start_list.pop(0)
                # temp_dict['Finish'] = finish_list.pop(0)
                # temp_dict['Resource'] = resource_list.pop(0)
                df.append(temp_dict)

            sol_line += "\n"
            sol_line_tasks += "\n"

        # print(sol_line_tasks)
        # print("Time Intervals for Tasks\n")
        # print(df)

        # return df
        draw_gantt_chart_div(df)
