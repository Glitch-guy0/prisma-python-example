#!/bin/sh

npx prisma migrate deploy
prisma generate
uvicorn main:app