from ft_package import count_in_list

import ft_package
print(ft_package.__name__)

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
