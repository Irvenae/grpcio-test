import grpc

if __name__ == '__main__':
    grpc.insecure_channel("localhost:8080")
    print("Ran succesfully.")