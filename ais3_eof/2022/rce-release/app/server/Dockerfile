FROM alpine:latest

RUN apk add clang musl-dev gcc

COPY check.c /check.c
COPY check.sh /check.sh
CMD ["/check.sh"]
