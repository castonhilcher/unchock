### Stage 1: build ###

FROM node:11.4.0-alpine as builder

# Set working directory.
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY unchock-ui/package.json unchock-ui/package-lock.json /app/unchock-ui/

# Install app dependencies.
RUN npm install --prefix unchock-ui

# Copy app files.
COPY . /app

# Build app
RUN npm run build --prefix unchock-ui -- --output-path=./dist/out

### Stage 2: delivery ###
FROM nginx:1.15.7-alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy output directory from builder to nginx image.
COPY --from=builder /app/unchock-ui/dist/out /usr/share/nginx/html

# Copy nginx configuration file.
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf