import subprocess


class Container:
    def __init__(self, IMAGE_NAME: str = "sandbox_python", container_name: str = "opensi_sandbox_service"):
        self.IMAGE_NAME = IMAGE_NAME
        self.container_name = container_name
        # checking if image exists
        self.check_if_image_exists()


    def check_if_image_exists(self):
        images = subprocess.run(f"docker images | grep {self.IMAGE_NAME}", shell=True, capture_output=True, text=True)
        if images.stdout.strip() == "":
            print("[INFO] Image does not exist")
            # print("[INFO] Building image...")
            # response = subprocess.run(f"docker build -t {self.IMAGE_NAME} .", shell=True)
            # print("[INFO] Image built")
            raise Exception("[ERROR] Image does not exist")
        else:
            print("[INFO] Image found")
    

    def check_if_container_exists(self) -> bool:
        containers = subprocess.run(f"docker ps -a | grep {self.container_name}", shell=True, capture_output=True, text=True)
        if containers.stdout.strip() == "":
             print("[INFO] Container does not exist")
        else:
            print("[INFO] Container found")

        return not containers.stdout.strip() == ""


    def create_container(self):
            print("[INFO] Creating container...")
            print("[INFO] Container created")
            # accepts mount volume
            # response = subprocess.run(f"docker run --name {self.container_name} -v {source_path}:/usr/src/app {self.IMAGE_NAME}", shell=True)
            # response = subprocess.run(f"docker run --name {self.container_name} --entrypoint /bin/bash -v $PWD:/usr/src/app sandbox_python", shell=True)
            # response = subprocess.run(f"docker run -it --name {self.container_name} --entrypoint /bin/bash -v /home/s448780/workspace/sandbox/opensi_ai_system:/usr/src/app sandbox_python", shell=True)
            response = subprocess.run(f"docker run --name {self.container_name} -v /home/s448780/workspace/sandbox/opensi_ai_system:/usr/src/app {self.IMAGE_NAME}", shell=True) # TODO: change path dynamic
            print(f"[PYCAPSULE-RESPONSE] {response.stdout}")
            print(f"[PYCAPSULE-EXIT CODE] {response.returncode}")
            return response.returncode, response.stdout, response.stderr
     
            
    def start_container(self):
        print("[INFO] Starting container...")
        response = subprocess.run(f"docker start -i {self.container_name}", shell=True, capture_output=True, text=True)
        print(f"[PYCAPSULE-RESPONSE] {response.stdout}")
        print(f"[PYCAPSULE-EXIT CODE] {response.returncode}")
        # print(f"[PYCAPSULE-ERROR] {"No error" if response.stderr == "" else response.stderr}")
        error_response = "No error" if response.stderr == "" else response.stderr
        print(f"[PYCAPSULE-ERROR] {error_response}")
        return response.returncode, response.stdout, response.stderr