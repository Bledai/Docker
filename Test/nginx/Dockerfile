FROM alpine
LABEL maintainer="Hanna Bledai"
RUN apk update && \
	apk add nginx && \
	rm -rf /var/cache/apk/* && \
	cat /etc/hosts 
COPY nginx.conf  /etc/nginx/nginx.conf
EXPOSE 80
ENTRYPOINT [ "nginx"]
CMD ["-g", "daemon off;"]
