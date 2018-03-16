
clean:
	rm -rf dist

build:
	mkdir -p dist
	tar -cvzf dist/minecraft-server-manager.wbm.gz minecraft-server-manager

reload:
	sudo rm -r /usr/share/webmin/minecraft-server-manager; sudo cp -r /vagrant/minecraft-server-manager /usr/share/webmin/minecraft-server-manager;

lint:
	perl -Mstrict -Mdiagnostics -cw minecraft-server-manager/msm-lib.pl
