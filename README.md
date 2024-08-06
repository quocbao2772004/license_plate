# The tutorial is for Windows systems and Linux.

<h2> If you have had a dataset, please skip step 1 and if you have had annaconda environment, please skip step 2 </h2>

<h3> Step1: Create a Dataset and label it by using labelimg </h3>

Clone the repository:

    git clone https://github.com/HumanSignal/labelImg.git
    
Convert resource files for PyQt5:    

<h4> Windows: </h4>

    pyrcc4 -o libs/resources.py resources.qrc
    For pyqt5, pyrcc5 -o libs/resources.py resources.qrc

<h4> Linux: </h4>

    sudo apt-get install pyqt5-dev-tools
    sudo pip3 install -r requirements/requirements-linux-python3.txt
    make qt5py3
    
Run LabelImg:  

    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
    
or:

    python3 labelImg.py
    python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

<h3> Step2: Create virtual environment </h3>

<h4> If you use Windows system: </h4>

  Install Anaconda and use the Anaconda Prompt to create a virtual environment:
  
     conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
     conda activate paddle_env
     
  Install required packages
  
     pip install -r requirements.txt

<h4> If you use Linux: </h4>

  Install annaconda:

    # First install wget
    sudo apt-get install wget # Ubuntu
    sudo yum install wget # CentOS
    
  Choose an annaconda version to install
  
      # Then use wget to download from Tsinghua source
    # If you want to download Anaconda3-2021.05-Linux-x86_64.sh, the download command is as follows
    wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2024.06-1-Linux-x86_64.exe
    # If you want to download another version, you need to change the file name after the last 1 / to the version you want to download
 To install Anaconda.

 - Type sh Anaconda3-2024.06-1-Linux-x86_64.sh at the command line
   
     - If you downloaded a different version, replace the file name of the command with the name of the file you downloaded
       
 - Just follow the installation instructions
   
     - You can exit by typing q when viewing the license
       
 - Add conda to the environment variables
    
     - If you have already added conda to the environment variable path during the installation, you can skip this step
    
     - Open ~/.bashrc in a terminal.
           
           # Enter the following command in the terminal.
            vim ~/.bashrc
       
     - Add conda as an environment variable in ~/.bashrc.

           # Press i first to enter edit mode # In the first line enter.
            export PATH="~/anaconda3/bin:$PATH"
            # If you customized the installation location during installation, change ~/anaconda3/bin to the bin folder in the customized installation directory
            
                   # The modified ~/.bash_profile file should look like this (where xxx is the username)
            export PATH="~/opt/anaconda3/bin:$PATH"
            # >>> conda initialize >>>
            # !!! Contents within this block are managed by 'conda init' !!!
            __conda_setup="$('/Users/xxx/opt/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
            if [ $? -eq 0 ]; then
               eval "$__conda_setup"
            else
               if [ -f "/Users/xxx/opt/anaconda3/etc/profile.d/conda.sh" ]; then
                   . "/Users/xxx/opt/anaconda3/etc/profile.d/conda.sh"
               else
                   export PATH="/Users/xxx/opt/anaconda3/bin:$PATH"
               fi
            fi
            unset __conda_setup
            # <<< conda initialize <<<
    When you are done, press esc to exit edit mode, then type :wq! and enter to save and exit
   
   - Verify that the Conda command is recognized.

    Enter source ~/.bash_profile in the terminal to update the environment variables
   
    Enter conda info --envs in the terminal again, if it shows that there is a base environment, then Conda has been added to the environment variables
   
  Create a new Conda environment
  
              # Enter the following command at the command line to create an environment called paddle_env
            # Here to speed up the download, use Tsinghua source
            conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
            
After install annaconda environment on Linux or Windows, you must install PaddleOcr

            pip3 install --upgrade pip
            
            # If you have cuda9 or cuda10 installed on your machine, please run the following command to install
            python3 -m pip install paddlepaddle-gpu==2.0.0 -i https://mirror.baidu.com/pypi/simple
            
            # If you only have cpu on your machine, please run the following command to install
            python3 -m pip install paddlepaddle==2.0.0 -i https://mirror.baidu.com/pypi/simple
            
<h3> Step3: Train a New Model or Use One of the Three Pre-trained YOLOv8 Models </h3>

      git clone https://github.com/quocbao2772004/license_plate.git

<h3> Step4: Using solve.py to see the results </h3>

    !python solve.py

![Screenshot 2024-07-29 105913](https://github.com/user-attachments/assets/965596dc-32ec-4dce-be47-fc1ddae7e3eb)

![Screenshot 2024-07-29 105852](https://github.com/user-attachments/assets/ff2f59e2-1d52-40bb-91f2-9f0d506350e9)

![Screenshot 2024-07-29 105831](https://github.com/user-attachments/assets/197a4104-3243-4c86-a633-ec67876bb647)

![Screenshot 2024-07-29 105928](https://github.com/user-attachments/assets/8c50a2f8-b12b-4ea8-82de-16e6e08e696f)

![Screenshot 2024-07-29 105928](https://github.com/user-attachments/assets/a405a33d-770b-4af6-81ac-60215fee57c4)

![image](https://github.com/user-attachments/assets/bc24cad6-6419-49a4-9b74-edad06bebb4f)

![image](https://github.com/user-attachments/assets/c4d28552-9a8f-41d1-b36f-8c86e39caba7)

![image](https://github.com/user-attachments/assets/609a76e0-bca9-4f8a-a8b8-57b9b9fb5582)

<h3> set up time </h3>

![image](https://github.com/user-attachments/assets/ea27a0fb-d259-4154-a266-3f814eb100b8)

![image](https://github.com/user-attachments/assets/6ebd7388-15f6-41f1-aff8-37d0e8baa308)

![image](https://github.com/user-attachments/assets/992ee222-8843-4a5e-bd50-d4a65d784e14)

![image](https://github.com/user-attachments/assets/3d5dacac-8810-43c1-a0f4-5974b615f6a8)

![image](https://github.com/user-attachments/assets/7337fc14-c965-4e44-8166-1f66a7dd1f94)

![image](https://github.com/user-attachments/assets/6ca05206-e73f-45e6-bc42-a7040085917a)

<h3> When using video() function, if we wanna stop the video, press the q key </h3>




