package service

import "com.skyfire.zn/models"

type Service interface {
	VerifyPassword(user, password string) error
	GetDoctorInfo(user string) ([]models.Doctor, error)
	GetDepartmentInfo(uid uint64) ([]models.Department, error)
	GetPatientsInfoByUid(uid uint64) ([]models.Patient, error)
	GetPatientsInfoByPid(pid uint64) ([]models.Patient, error)
	GetPatientsInfoByDid(did uint64) ([]models.Patient, error)
	GetPatientsInfoByUName(uname string) ([]models.Patient, error)
	GetFileTypeList() ([]models.FileType, error)

	AppendFile(fi models.FileInfo) error
	GetFileInfoList(pid uint64) ([]models.FileInfo, error)
	GetFileInfoByFid(fid uint64) (*models.FileInfo, error)
}
