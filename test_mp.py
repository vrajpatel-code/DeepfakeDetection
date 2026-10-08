import multiprocessing as mp

def f():
    try:
        import torch
        print('torch imported successfully in child')
    except Exception as e:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    mp.set_start_method('spawn')
    p = mp.Process(target=f)
    p.start()
    p.join()
