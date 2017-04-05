from pyrouge import Rouge155

r = Rouge155('/home/sudarshan/Downloads/RELEASE-1.5.5/')
r.system_dir = '/home/sudarshan/Desktop/TheChainRanker/RougeEval/syssum/suraj/'
r.model_dir = '/home/sudarshan/Desktop/TheChainRanker/RougeEval/modsum/'
r.system_filename_pattern = 'summary_(\d+).txt'
#r.model_filename_pattern = 'bootest.[A-Z].#ID#.txt'
r.model_filename_pattern = 'summary_#ID#.txt'

output = r.convert_and_evaluate()
f = open('respg.txt','w')
f.write(output)
output_dict = r.output_to_dict(output)
print (output_dict)
f.close()