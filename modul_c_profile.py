import cProfile
import pstats

cProfile.run('import main_gra', 'rezultat_profilowania.prof')

stats = pstats.Stats('rezultat_profilowania.prof')
stats.strip_dirs()
stats.sort_stats('cumulative') 
stats.print_stats(30) 
