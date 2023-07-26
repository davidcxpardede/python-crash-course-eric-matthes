from user_module import User
from admin_privileges import Admin, Privileges

privilege_1 = Privileges(['can add users', 'can remove users', 'can message users'])
admin_1 = Admin('david', 'pardede', 13618012, 'ftmd', 'aerospace engineering', privilege_1)

admin_1.privileges.show_privileges()