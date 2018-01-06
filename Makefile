
schemas = acct.xsd \
	cluster_pool.xsd \
	cluster.xsd \
	datastore_pool.xsd \
	datastore.xsd \
	group_pool.xsd \
	group.xsd \
	host_pool.xsd \
	host.xsd \
	image_pool.xsd \
	image.xsd \
	marketplaceapp_pool.xsd \
	marketplaceapp.xsd \
	marketplace_pool.xsd \
	marketplace.xsd \
	user_pool.xsd \
	user.xsd \
	vdc_pool.xsd \
	vdc.xsd \
	vm_pool.xsd \
	vmtemplate_pool.xsd \
	vmtemplate.xsd \
	vm.xsd \
	vnet_pool.xsd \
	vnet.xsd \
	vrouter_pool.xsd \
	vrouter.xsd 
 

VPATH = src: pyone/xsd

all: pyone/bindings/__init__.py

pyone/bindings/__init__.py: $(schemas)
	pyxbgen -m pyone.bindings.__init__ -u $^

.PHONY: clean
clean: 
	rm -f pyone/bindings/*.py
