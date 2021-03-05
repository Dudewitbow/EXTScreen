import tkinter as tk
import wmi

class mainWindow:
    def __init__(self, master=None):
        self.master = master
        master.title("Temperature/Image Server")
        #Open Hardware Monitor WMI data
        self.localTemp = wmi.WMI(namespace="root\OpenHardwareMonitor")
        #grabbing WMI default name
        self.cpuNameContainer = wmi.WMI()

        #CPU name information
        self.cpuFrame = tk.Frame(bg="#202020")
        self.cpuFrame.grid(row=0, column=0, sticky='ew')
        self.cpu = "CPU Name: " + self.getCPUName()
        self.cpuName = tk.Label(self.cpuFrame, text=self.cpu, fg="#e6e6e6", bg="#202020")
        self.cpuName.grid(row=0, column=0)

        #CPU Clock information
        self.clockFrame = tk.Frame(bg="#202020")
        self.clockFrame.grid(row=1, column=0, sticky='ew')
        self.clock = "CPU Clock: "
        self.clockLabel = tk.Label(self.clockFrame, text=self.clock, fg="#e6e6e6", bg="#202020")
        self.clockLabel.grid(row=1, column=0)
        self.clockValue = tk.Label(self.clockFrame, text="0", fg="#e6e6e6", bg="#202020")
        self.clockValue.grid(row=1, column=1)

        #CPU temp information
        self.tempFrame = tk.Frame(bg="#202020")
        self.tempFrame.grid(row=2, column=0, sticky='ew')
        self.cpuTemp = "Temp: "
        self.cpuTempLabel = tk.Label(self.tempFrame, text=self.cpuTemp, fg="#e6e6e6", bg="#202020")
        self.cpuTempLabel.grid(row=2, column=0)
        self.tempValue = tk.Label(self.tempFrame, text="0", fg="#e6e6e6", bg="#202020")
        self.tempValue.grid(row=2, column=1)

        #recursive update
        self.master.after(1000, self.update)

    def update(self):
        #Temp Update
        temps = self.localTemp.Sensor()
        temp = " "
        clock = " "
        count = 0
        for sensor in temps:
            if sensor.SensorType==u'Temperature' and sensor.Name=='CPU Package' :
                temp = sensor.Value
                count+=1
            if sensor.SensorType==u'Clock' and sensor.Name== 'CPU Core #1':
                clock = sensor.Value
                count+=1
            if count==2:
                break
        self.tempValue["text"] = str(temp)
        self.clockValue["text"] = str(int(clock))

        self.master.after(1000, self.update)
    
    def getCPUName(self):
            return self.cpuNameContainer.Win32_Processor()[0].name

def main():
    root = tk.Tk()
    root.configure(bg="#202020")
    server = mainWindow(master=root)
    root.mainloop()


if __name__ == "__main__":
    main()