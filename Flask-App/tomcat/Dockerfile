FROM alpine
LABEL maintainer="Hanna Bledai"
RUN apk update && \
	apk add openjdk8 && \
	cd /opt && \
	wget  http://ftp.byfly.by/pub/apache.org/tomcat/tomcat-9/v9.0.20/bin/apache-tomcat-9.0.20.tar.gz && \
    tar xvzf /opt/apache-tomcat-9.0.20.tar.gz && \
    mv /opt/apache-tomcat-9.0.20 /opt/tomcat && \
    rm -rf /opt/*.tar.gz
COPY catalina.sh /opt/tomcat/bin/catalina.sh
EXPOSE 8080

CMD ["/opt/tomcat/bin/catalina.sh", "run"]
