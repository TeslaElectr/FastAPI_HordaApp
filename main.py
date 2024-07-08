from app import init_app


app = init_app()


def uvicorn_run():
    import uvicorn

    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
    )


def sys_path():
    import sys
    print(sys.path)
    

if __name__ == "__main__":
    uvicorn_run()
    # sys_path()