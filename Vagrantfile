Vagrant.configure("2") do |config|
  # This fixes some serious performance issues with the virtual machine
  # network interfaces. Solution pulled from stack overflow:
  # https://stackoverflow.com/questions/27401513/vagrant-ansible-resolving-super-slow
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
  end

  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 2
  end
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "public_network"
end