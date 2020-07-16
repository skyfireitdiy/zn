package service

import (
	database "com.skyfire.zn/database"
	"com.skyfire.zn/models"
)

type ServiceImpl struct {
	db *database.Database
}

func NewService(db *database.Database) Service {
	return &ServiceImpl{
		db: db,
	}
}

func (*ServiceImpl) VerifyPassword(user, password string) error {
	return nil
}
func (*ServiceImpl) GetDoctorInfo(user string) ([]models.Doctor, error) {
	return nil, nil
}
func (*ServiceImpl) GetDepartmentInfo(uid uint64) ([]models.Department, error) {
	return nil, nil
}
func (*ServiceImpl) GetPatientsInfoByUid(uid uint64) ([]models.Patient, error) {
	return nil, nil
}
func (*ServiceImpl) GetPatientsInfoByPid(pid uint64) ([]models.Patient, error) {
	return nil, nil
}
func (*ServiceImpl) GetPatientsInfoByDid(did uint64) ([]models.Patient, error) {
	return nil, nil
}
func (*ServiceImpl) GetPatientsInfoByUName(uname string) ([]models.Patient, error) {
	return nil, nil
}
func (*ServiceImpl) GetFileTypeList() ([]models.FileType, error) {
	return nil, nil
}
func (*ServiceImpl) AppendFile(fi models.FileInfo) error {
	return nil
}
func (*ServiceImpl) GetFileInfoList(pid uint64) ([]models.FileInfo, error) {
	return nil, nil
}
func (*ServiceImpl) GetFileInfoByFid(fid uint64) (*models.FileInfo, error) {
	return nil, nil
}
