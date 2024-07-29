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

      git clone https://github.com/quocbao2772004/license_plate.git

Step4: Using solve.py to see the results

    !python solve.py

![Screenshot 2024-07-29 105913](https://github.com/user-attachments/assets/965596dc-32ec-4dce-be47-fc1ddae7e3eb)

![Screenshot 2024-07-29 105852](https://github.com/user-attachments/assets/ff2f59e2-1d52-40bb-91f2-9f0d506350e9)

![Screenshot 2024-07-29 105831](https://github.com/user-attachments/assets/197a4104-3243-4c86-a633-ec67876bb647)

![Screenshot 2024-07-29 105928](https://github.com/user-attachments/assets/8c50a2f8-b12b-4ea8-82de-16e6e08e696f)

![Screenshot 2024-07-29 105928](https://github.com/user-attachments/assets/a405a33d-770b-4af6-81ac-60215fee57c4)


When using video() function, if we wanna stop the video, press the q key




