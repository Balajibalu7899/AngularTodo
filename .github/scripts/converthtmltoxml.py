
import  jpype     
import  asposecells     
jpype.startJVM() 
from asposecells.api import Workbook
workbook = Workbook("input.html");
workbook.Save("Output.xml");
jpype.shutdownJVM()
