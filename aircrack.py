# Executing, communicating with, killing processes
from subprocess import Popen, call, PIPE


class Aircrack:


    def check_executables(self):
        None


    def exec_exists(self, program):
        """
            Uses 'which' (linux command) to check if a program is installed.
        """

        proc = Popen(['which', program], stdout=PIPE, stderr=PIPE)
        txt = proc.communicate()
        if txt[0].strip() == '' and txt[1].strip() == '':
            return False
        if txt[0].strip() != '' and txt[1].strip() == '':
            return True

        return not (txt[1].strip() == '' or txt[1].find('no %s in' % program) != -1)


