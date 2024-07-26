
Step1: Create a Dataset and label it by using labelimg

    git clone https://github.com/HumanSignal/labelImg.git
    pyrcc4 -o libs/resources.py resources.qrc
    For pyqt5, pyrcc5 -o libs/resources.py resources.qrc
  
    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

Step2: Create virtual environment
  Installing annaconda and using annaconda prompt to create virtual environment
  
     conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
     conda activate paddle_env
     pip install -r requirements.txt

Step3: Train model by YOLOv8 and we have 3 pretrained models

Step4: Using solve.py to see the results

    !python solve.py

![image](https://github.com/user-attachments/assets/c5baa16e-f5cd-4f27-97f1-7657e30ac4c8)

![image](https://github.com/user-attachments/assets/584c8f0b-a2d3-4b9b-abb8-829c608729b5)

![image](https://github.com/user-attachments/assets/863bcc62-e5f4-4470-a51e-361c08c0142b)

![image](https://github.com/user-attachments/assets/1e50157e-b8ea-45d4-8796-1e79bb7f60ef)

![image](https://github.com/user-attachments/assets/a8916b9d-6503-4158-8367-12575d1c2e50)

When using video() function, if we wanna stop the video, press the q key




