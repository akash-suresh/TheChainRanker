from pyrouge import Rouge155

r = Rouge155('/home/sudarshan/Downloads/RELEASE-1.5.5/')
r.system_dir = 'syssum/'
r.model_dir = 'modsum/'
r.system_filename_pattern = 'bootest.(\d+).txt'
r.model_filename_pattern = 'bootest.[A-Z].#ID#.txt'

output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)