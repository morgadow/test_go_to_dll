@echo off & setlocal

go build -buildmode c-shared -o lib.so lib.go
go build -buildmode c-shared -o lib.dll lib.go

