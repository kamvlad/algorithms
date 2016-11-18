processes = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

processes.sort(cmp = (lambda x, y :  -1 if x[1] < y[1] else 1))

def isInterleaved(a, b):
    return not(a[0] >= b[1] or b[0] >= a[1])

def chooseProcessesRecurcive(processId, processes, dynamicTable):
    if (dynamicTable[processId] != -1):
        return dynamicTable[processId]

    if processId == -1:
        return (0, set())

    notInterleavedProcessId = processId
    while isInterleaved(processes[notInterleavedProcessId], processes[processId]) and notInterleavedProcessId > -1:
        notInterleavedProcessId -= 1

    withThisProcess = chooseProcessesRecurcive(notInterleavedProcessId, processes, dynamicTable)
    withThisProcess = (withThisProcess[0] + 1, withThisProcess[1] | set([processes[processId]]))
    withoutThisProcess = chooseProcessesRecurcive(processId - 1, processes, dynamicTable)

    if (withThisProcess > withoutThisProcess):
        dynamicTable[processId] = withThisProcess
    else:
        dynamicTable[processId] = withoutThisProcess

    return dynamicTable[processId]

def chooseProcesses(processes):
    return chooseProcessesRecurcive(len(processes) - 1, processes, [-1] * len(processes))

print(chooseProcesses(processes))