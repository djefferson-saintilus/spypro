import os
import importlib,time
import colorama
from colorama import Fore, Style
import config.func.functions as fc

fc.manual()  # help
colorama.init()


class SpyPro:
    def __init__(self):
        self.banner = True
        self.max_invalid_choices = 3
    
    def show_banner(self):
        os.system('clear')  # Clear screen
        fc.bannerSpyPro()
    
    def main_menu(self):
        self.verify_initialization()
        
        while True:
            self.show_banner()
            fc.menu()
            invalid_choices = 0
            
            while invalid_choices < self.max_invalid_choices:
                try:
                    choice = int(input("sp1 > "))
                    if choice == 0:
                        print(f"{Fore.GREEN}Thanks for using SpyPro, bye !!!{Style.RESET_ALL}")
                        return
                    elif choice not in range(1, 6):
                        print(f"{Fore.RED}Invalid option. Please enter a number between 1 and 5.{Style.RESET_ALL}")
                        invalid_choices += 1
                    else:
                        if choice == 1:
                            self.info_gathering_menu()
                        elif choice == 2:
                            print("Please wait")
                        elif choice == 3:
                            print("Please wait")
                        elif choice == 4:
                            print("Please wait")
                        elif choice == 5:
                            print("Please wait")
                        
                        print(f"{Fore.GREEN}Thanks for using SpyPro{Style.RESET_ALL}")
                        input("Press Enter to continue...")
                        break
                except ValueError:
                    print(f"{Fore.RED}Invalid option. Please enter a number between 1 and 5.{Style.RESET_ALL}")
                    invalid_choices += 1
                
                if invalid_choices == self.max_invalid_choices:
                    print(f"{Fore.RED}Max invalid choices reached. Exiting...{Style.RESET_ALL}")
                    return
    
    def info_gathering_menu(self):
        while True:
            self.show_banner()
            fc.menuInfoGathering()
            invalid_choices = 0
            
            while invalid_choices < self.max_invalid_choices:
                try:
                    choice1 = int(input("sp1 > "))
                    if choice1 == 0:
                        return
                    elif choice1 not in range(1, 8):
                        print(f"{Fore.RED}Invalid option. Please enter a number between 1 and 7.{Style.RESET_ALL}")
                        invalid_choices += 1
                    else:
                        if choice1 == 1:
                            try:
                                fc.osDiscovery()
                            except FileNotFoundError:
                                print(f"{Fore.RED}File not found!{Style.RESET_ALL}")
                        elif choice1 == 2:
                            try:
                                fc.basicNmap()
                            except FileNotFoundError:
                                print(f"{Fore.RED}File not found!{Style.RESET_ALL}")
                        elif choice1 == 3:
                            try:
                                fc.dirListing()
                            except FileNotFoundError:
                                print(f"{Fore.RED}File not found!{Style.RESET_ALL}")
                        elif choice1 == 4:
                            try:
                                fc.check_robots_txt()
                            except FileNotFoundError:
                                print(f"{Fore.RED}File not found!{Style.RESET_ALL}")
                        elif choice1 == 5:
                            print("Please wait ...")
                        elif choice1 == 6:
                            print("Please wait ...")
                        elif choice1 == 7:
                            print("Please wait ...")
                        
                        input("Press Enter to continue...")
                        break
                except ValueError:
                    print(f"{Fore.RED}Invalid option. Please enter a number between 1 and 7.{Style.RESET_ALL}")
                    invalid_choices += 1
                
                if invalid_choices == self.max_invalid_choices:
                    print(f"{Fore.RED}Max invalid choices reached. Exiting...{Style.RESET_ALL}")
                    return
    
    def verify_initialization(self):
        print("Verifying initialization...")
        print("Please wait ...")
        
        # Progress indicator
        progress_symbols = ["|", "/", "-", "\\"]
        start_time = time.time()
        elapsed_time = 0
        
        while elapsed_time < 2:
            for symbol in progress_symbols:
                print(f"\r{symbol} Verifying...", end="", flush=True)
                time.sleep(0.2)
            
            elapsed_time = time.time() - start_time
        
        print("\rVerification complete!          ")
        print()
        
        # Check for required files
        file_paths = [
            "config/func/functions.py",
            "config/bannerOfficial.txt",
            "requirements.txt"

            # Add other required file paths here
        ]
        missing_files = []
        for file_path in file_paths:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        # Verify modules
        modules = [
            "config.func.functions",
            # Add other required modules here
        ]
        missing_modules = []
        for module_name in modules:
            try:
                importlib.import_module(module_name)
            except ModuleNotFoundError:
                missing_modules.append(module_name)
        
        # Display summary
        if not missing_files and not missing_modules:
            print(f"{Fore.GREEN}Initialization successful. All required files and modules found.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Initialization failed. The following files or modules are missing:{Style.RESET_ALL}")
            if missing_files:
                print(f"{Fore.RED}Missing Files:{Style.RESET_ALL}")
                for file_path in missing_files:
                    print(f"  {file_path}")
            if missing_modules:
                print(f"{Fore.RED}Missing Modules:{Style.RESET_ALL}")
                for module_name in missing_modules:
                    print(f"  {module_name}")
            exit(1)

    def run(self):
        try:
            self.main_menu()
        except KeyboardInterrupt:
            print(f"{Fore.RED}\nProgram interrupted. Exiting...{Style.RESET_ALL}")


if __name__ == "__main__":
    spy_pro = SpyPro()
    spy_pro.run()
