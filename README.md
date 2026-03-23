## MadBook

This is a lightweight bookkeeping APP that supports multiple ledgers and statistical analysis functions, and the mobile experience is better. This project adopts the design of separating the front and back end, the backend is built using the FastAPI framework, and the front end uses boostrap & jQuery for lightweight. In fact, there is only one web page in the entire front-end section, and all subpages are dynamically rendered. Here are some screenshots of the run.

This is a lightweight bookkeeping app that supports multiple ledgers and statistical analysis functions. The mobile terminal has a better experience.
The project adopts a front-end and back-end separation design, the back-end is built using the fastapi framework, and the front-end uses bootstrap & jQuery for lightweight.
In fact, there is only one web page in the whole front end, and all sub pages are rendered dynamically. Running screenshots:

![运行截图](docs/demo.jpg)

You can run it with a simple configuration, requiring:

Python3.7+
MongoDB (dependencies)
It is recommended to use Docker for deployment and running, and you can use the docker-compose tool to run with the dependent MongoDB container with one click. For MongoDB databases, you can refer to the following to build a database:
[docker.com/_/mongo](https://hub.docker.com/_/mongo)

### deployment
Native Python environment deployment:  
```shell
export MAD_BOOK_MONGODB_URL="xxx"   # 后端数据库，示例: "mongodb://{mongo_user}:{mongo_password}@{host:port}/{db_name}"
export PASSWORD_ENCRYPT_SALT="xxx"  # 加密用户密码之用，[a-z|A-Z|0-9]字符串，长度32
export TOKEN_ENCRYPT_SALT="xxx"     # 加密登录token之用，[a-z|A-Z|0-9]字符串，长度32
export REG_KEY="xxx"                # 注册码，长度任意。可不设置，默认值"test_1234"

pip install -r requirements.txt
sh startup.sh
```

Docker部署：
```shell
imageName="madbook"
docker build -t ${imageName} .
docker run -d -p 1992:1992 \
    -e MAD_BOOK_MONGODB_URL="xxx" \
    -e PASSWORD_ENCRYPT_SALT="xxx" \
    -e TOKEN_ENCRYPT_SALT="xxx" \
    -e REG_KEY="xxx" \
    ${imageName}
```

Then, the browser accesses the http://localhost:1992/madbook pop-up login page to indicate that the deployment has been successful.

---
This project is open source under the GPLv3 license.
