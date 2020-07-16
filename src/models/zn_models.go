package models

import "time"

type FileInfo struct {
	ID        string
	FileName  string
	Type      string
	Size      uint64
	UpTime    time.Time
	LocalPath string
	Pid       string
	Uid       string
}

type Doctor struct {
}

type Department struct {
}

type Patient struct {
}

type FileType struct {
}
