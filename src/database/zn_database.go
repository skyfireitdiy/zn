package database

import (
	"github.com/go-xorm/xorm"
	_ "github.com/mattn/go-oci8"
	_ "github.com/mattn/go-sqlite3"
	"xorm.io/core"
)

type Database struct {
	publicEngine *xorm.Engine
	localEngine  *xorm.Engine
}

func NewDatabase(publicDataSource, localDataSource string) (*Database, error) {
	ret := &Database{}
	var err error
	ret.publicEngine, err = xorm.NewEngine("oci8", publicDataSource)
	if err != nil {
		return nil, err
	}

	ret.localEngine, err = xorm.NewEngine("sqlite3", localDataSource)
	if err != nil {
		ret.publicEngine.Close()
		return nil, err
	}
	return ret, nil
}

func (db *Database) Close() {
	db.publicEngine.Close()
	db.localEngine.Close()
}

func (db *Database) GetPublicTables() ([]*core.Table, error) {
	return db.publicEngine.DBMetas()
}
