from tester import Tester

def main():
    tester = Tester()

    # tester.random_test_rbfs(x = 12, y = 12, loop_percent = 15, visualize = True, print_path = True)
    tester.random_test_dls(x = 15, y = 15, limit = 15 * 15 // 3, loop_percent = 5, visualize = True, print_path = True) 
    # tester.test_rbfs() 
    # tester.test_dls()   

if __name__ == "__main__":
    main()
