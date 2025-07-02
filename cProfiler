import cProfile
import pstats

cProfile.run('import main_gra', 'profiling_results.prof')

stats = pstats.Stats('profiling_results.prof')
stats.strip_dirs()
stats.sort_stats('cumulative')  # Możesz zmienić na 'time', 'calls', itp.
stats.print_stats(30)  # Pokaż top 30 najbardziej kosztownych funkcji
