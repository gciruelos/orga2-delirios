import statistics
import matplotlib.pyplot as plt
import matplotlib

font = {'size' : 22}

matplotlib.rc('font', **font)
f = open('tiempos/tiempos.txt', 'r')
MICRO = 1000000.0

r = {}
for i in range(10):
    name = f.readline().split()[0]
    nums = []
    for _ in range(500):
        line = list(map(float, f.readline().split()))
        if line[0] < 0 or line[1] < 0 or line[2] < 0:
            print('WARNING: %s' % line)
            continue
        nums.append(line)
    r[name] = nums

experimentos = ['create', 'write', 'remove', 'read', 'mkdir']

resultados = {
    'create' : {},
    'write' : {},
    'remove' : {},
    'read' : {},
    'mkdir' : {}
}
for exp in experimentos:
    resultados[exp]['read'] = list(
            map(lambda x: MICRO*x[0], r['delirios_%s' % exp]))
    resultados[exp]['write'] = list(
            map(lambda x: MICRO*x[1], r['delirios_%s' % exp]))
    resultados[exp]['delirios'] = list(
        map(lambda x: MICRO*x[2], r['delirios_%s' % exp]))
    resultados[exp]['linux'] = list(
            map(lambda x: MICRO*x[2], r['linux_%s' % exp]))

for exp in experimentos:
    print('Experimento: %s.' % exp)
    print('  read     -> %f' % min(resultados[exp]['read']))
    print('  write    -> %f' % min(resultados[exp]['write']))
    print('  delirios -> %f' % min(resultados[exp]['delirios']))
    print('  linux    -> %f' % min(resultados[exp]['linux']))


for i, exp in enumerate(experimentos):
    delirios = resultados[exp]['delirios']
    linux = resultados[exp]['linux']
    fix, ax = plt.subplots()
    plt.boxplot(
            [delirios, linux],
            labels=['delirios', 'linux'],
            widths=0.5,
    )
    plt.title(exp)
    plt.ylabel("Tiempo (us)")
    ax.set_ylim(0.0, max(statistics.mean(delirios), statistics.mean(linux))*1.3)
    plt.xlabel("Sistema Operativo")
    plt.savefig('tiempos/'+exp+'.pdf', bbox_inches='tight')

delirios_write = [4,3,2,2,2,2,2,2,3,1,2,2,2,2,2,2,1,2,3,2,1]
delirios = list(map(lambda r: r*122.0, delirios_write))
linux = resultados['write']['linux']
fix, ax = plt.subplots()
plt.boxplot(
	[delirios, linux],
	labels=['delirios', 'linux'],
	widths=[0.5, 0.5],
)
plt.title('write')
plt.ylabel("Tiempo (us)")
ax.set_ylim(0.0, 500.0)
plt.xlabel("Sistema Operativo")
plt.savefig('tiempos/delirios_linux.pdf', bbox_inches='tight')


