---
title: Git
layout: post
date: '2016-12-23 11:26:03'
tags:
- git
---

## 동작 원리 
- branch
	- Master 브랜치 :  언제든지 릴리즈가 가능한 형태여야 한다.(서비스가 가능한 코드)
	- hotfix 브랜치 : 심각한 오류가 발견된 상태
	- Release 브랜치 : 
	- Develope 브랜치 : 
	- Feature 브랜치 : 실질적으로 작업을 하는 브랜치

- snapshot
- checksum
	- 데이터를 저장하기 전 체크섬을 구하고, 이 체크섬을 통해서 데이터를 관리한다. 
	- 파일 이름이 아닌 컨텐츠의 해쉬 값을 저장(SHA-1 해쉬 사용).
	- commit할 때의 16자리 id값. 

- Section
	- Working directory
		- 작업자가 작업하는 디렉토리.
	- Staging Area
		- 작업자가 디렉토리에 추가하면 깃에 추가 되는데, 이 단계를 일컫는다.
	- Repository
		- 원격 저장소. (commit을 통해서 올린다.)

## Git은 **책임성**을 유지하기 위해 커밋한 사람의 *이메일*과 *이름*이 반드시 필요하다. 

Git Configuration file location
1. System global path
	- [MAC OS] : git config --global --edit
2. USER_HOME/.gitconfig
	- 사용자별 설정 정보
	- git config --global user.name NAME
	- git config --global user.email NAME@XXX.XX
3. PROJECT_DIRECTORY/XXX/.git/config

## Git Workflow
- Init
	- get init : 현재 디렉토리를 git 레포지토리로 설정. 
- Ignore
	- .ignore 파일에 버전관리 하지 않을 파일들의 목록을 적는다.
- Status
- Add
- Commit
- Log
- Diff
- Branch
- Tag
- Checkout
- Merge