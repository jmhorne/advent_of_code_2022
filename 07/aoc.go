package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Directory struct {
	Name    string
	Parent  *Directory
	Size    uint64
	SubDirs map[string]*Directory
	Files   map[string]uint64
}

func NewDirectory(name string, parent *Directory, output []string) *Directory {
	d := new(Directory)
	d.Name = name
	d.Parent = parent
	d.Size = 0
	d.SubDirs = make(map[string]*Directory)
	d.Files = make(map[string]uint64)

	if output != nil {
		d.Parse_output(output)
	}

	return d
}

func (d *Directory) Parse_output(output []string) {
	currDir := d

	for len(output) != 0 {
		fmt.Println("output size: ", len(output), currDir.Name, output[0])
		line := strings.Split(output[0], " ")
		output = output[1:]

		if line[0] == "$" {
			if line[1] != "cd" {
				continue
			}

			if line[2] == ".." {
				currDir = currDir.Parent
			} else if _, ok := d.SubDirs[line[2]]; !ok {
				newDir := NewDirectory(line[2], currDir, nil)
				d.SubDirs[line[2]] = newDir
				currDir = newDir
			} else {
				currDir = d.SubDirs[line[2]]
			}

		} else if line[0] == "dir" {
			currDir.SubDirs[line[1]] = NewDirectory(line[1], currDir, nil)
		} else {
			fmt.Printf("Adding file: %v\n", line)
			i, _ := strconv.ParseInt(line[0], 10, 64)
			currDir.Size += uint64(i)
			currDir.Files[line[1]] = uint64(i)
		}

		// if line[0] == "$" {
		// 	if line[1] == "cd" {
		// 		fmt.Println("CDing to ", line[2])
		// 		if line[2] == ".." {
		// 			currDir = currDir.Parent
		// 		} else if _, ok := d.SubDirs[line[2]]; !ok {
		// 			newDir := NewDirectory(line[2], currDir, output)
		// 			d.SubDirs[newDir.Name] = newDir
		// 			currDir = newDir
		// 		} else {
		// 			currDir = d.SubDirs[line[2]]
		// 		}

		// 	}else if line[1] == "ls" {
		// 		for len(output) != 0 {
		// 			if output[0][0] == '$' {
		// 				break
		// 			}
		// 			line = strings.Split(output[0], " ")
		// 			output = output[1:]

		// 			if line[0] == "dir" {
		// 				fmt.Println("adding dir: ", line[1])
		// 				currDir.SubDirs[line[1]] = NewDirectory(line[1], currDir, nil)
		// 			} else {
						// fmt.Printf("Adding file: %v\n", line)
						// i, _ := strconv.ParseInt(line[0], 10, 64)
						// currDir.Size += uint64(i)
						// currDir.Files[line[1]] = uint64(i)
		// 			}
		// 		}
		// 	}
		// }
	}
}

func (d *Directory) AddDir(dir *Directory) {
	d.SubDirs[dir.Name] = dir
}

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatalln("can't find input file")
	}

	output := strings.Split(string(file), "\n")

	cmd := strings.Split(output[0], " ")
	output = output[1:]
	var root *Directory = NewDirectory(cmd[2], nil, output)

	fmt.Printf("size: %d\n", root.Size)
}
