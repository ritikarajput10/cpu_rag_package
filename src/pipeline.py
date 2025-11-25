import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generate import rag

def run_pipeline():
    while True:
        q = input("\nAsk: ")
        print("\nAnswer:")
        print(rag(q))

if __name__ == "__main__":
    run_pipeline()
