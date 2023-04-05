from carthage import *
from carthage.modeling import *
from carthage.podman import *
from carthage.oci import *

class Layout(CarthageLayout):

    add_provider(machine_implementation_key, dependency_quote(PodmanContainer))

    class test_image(ContainerfileImageModel):
        oci_image_tag = 'localhost/test/test-image:latest'
        container_context = 'test-image'

    class test(MachineModel):
        add_provider(oci_container_image, test_image)
