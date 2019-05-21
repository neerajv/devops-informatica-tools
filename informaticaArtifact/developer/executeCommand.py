#  MIT License
#
#  Copyright (c) 2019 Jac. Beekers
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

from supporting import log
import logging
import supporting.errorcodes as errorcodes
import subprocess
import os

logger = logging.getLogger(__name__)
entrynr =0

errorMessage =errorcodes.INFACMD_FAILED.message

def execute(command):
    env = {**os.environ, 'NO_ENV': 'TRUE'}
    execute(command, env)


def execute(command, env):
    thisproc = "execute"
    process = ""
    result = errorcodes.OK

    log(logger, logging.DEBUG, thisproc, "Executing command >" + command + "<.")

    pipes = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, env=env)
    pipes.wait()
    std_out, std_err = pipes.communicate()

    if pipes.returncode == 0:
        log(logger, logging.INFO, thisproc, std_out.decode("utf-8"))
    else:
        result = errorcodes.COMMAND_FAILED
        result.message = std_out.decode("utf-8") + std_err.decode("utf-8")
        log(logger, logging.ERROR, thisproc, result.message)

    return result
