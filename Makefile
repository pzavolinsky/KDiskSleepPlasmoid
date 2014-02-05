.PHONY: test package install remove

test:
	plasmoidviewer .

package:
	@echo -e "\n[PACKAGE]"
	zip -x Makefile -x disksleep.zip -r /tmp/disksleep.zip .
	mv /tmp/disksleep.zip .

install: package
	AUX=$(plasmapkg -l | grep "Disk-Sleep-Plasmoid"); if [ ! -z "$AUX" ]; then $(MAKE) --no-print-directory remove; fi
	@echo -e "\n[INSTALL]"
	plasmapkg -i disksleep.zip

remove:
	@echo -e "\n[REMOVE]"
	plasmapkg -r "Disk-Sleep-Plasmoid"
