# The tutorial is only for Windows systems.

Step1: Create a Dataset and label it by using labelimg

Clone the repository:

    git clone https://github.com/HumanSignal/labelImg.git
    
Convert resource files for PyQt5:    

    pyrcc4 -o libs/resources.py resources.qrc
    For pyqt5, pyrcc5 -o libs/resources.py resources.qrc
    
Run LabelImg:  

    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

Step2: Create virtual environment

  Install Anaconda and use the Anaconda Prompt to create a virtual environment:
  
     conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
     conda activate paddle_env
     
  Install required packages
  
     pip install -r requirements.txt

Step3: Train a New Model or Use One of the Three Pre-trained YOLOv8 Models

      git clone https://github.com/quocbao2772004/plate.git

Step4: Using solve.py to see the results

    !python solve.py

![image](https://github.com/user-attachments/assets/c5baa16e-f5cd-4f27-97f1-7657e30ac4c8)

![image](https://github.com/user-attachments/assets/584c8f0b-a2d3-4b9b-abb8-829c608729b5)

![image](https://github.com/user-attachments/assets/863bcc62-e5f4-4470-a51e-361c08c0142b)

![image](https://github.com/user-attachments/assets/1e50157e-b8ea-45d4-8796-1e79bb7f60ef)

![image](https://github.com/user-attachments/assets/a8916b9d-6503-4158-8367-12575d1c2e50)

When using video() function, if we wanna stop the video, press the q key




