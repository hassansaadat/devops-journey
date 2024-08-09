# Self-signed TLS Secret Creation

```shell
# Generate a private key
openssl genrsa -out dashboard.key 2048
```

```shell
# Generate a self-signed certificate
openssl req -new -x509 -key dashboard.key -out dashboard.crt -days 365 -subj "/CN=dashboard.com"
```

make base 64
```shell
echo -n dashboard.key | base64
echo -n dashboard.crt | base64
```
