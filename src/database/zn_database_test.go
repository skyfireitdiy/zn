package database

import (
	"testing"
)

func TestDatabaseOpen(t *testing.T) {
	db, err := NewDatabase("app/app123456@114.115.140.157:1521/orcl", "./fileinfo.db")
	if err != nil {
		t.Error(err.Error())
		return
	}
	defer db.Close()

	tbs, err = db.GetPublicTables()
	if err != nil {
		t.Error(err)
		return
	}

	t.Logf("get table count: %d\n", len(tbs))
	for _, t := range tbs {
		t.Logf("table name: %s\n", t.Name)
	}
}
