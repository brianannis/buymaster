nodes = [
  { hostname: 'node-01', box: 'bento/ubuntu-16.04' }
]

Vagrant.configure('2') do |config|

  # Configure our boxes with 1 CPU and 512MB of RAM
  config.vm.provider 'vmware_fusion' do |v|
    v.cpus = '2'
    v.memory = '2048'
  end

  # Go through nodes and configure each of them.j
  nodes.each do |node|
    config.vm.define node[:hostname] do |node_config|
      node_config.vm.box = node[:box]
      node_config.vm.hostname = node[:hostname]
      node_config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/core.yml"
      end
    end
  end
end
