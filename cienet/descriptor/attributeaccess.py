#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Base:

    base_class_attr = 0

    def __init__(self):
        self.base_instance_attr = 1


class Derive(Base):

    derive_class_attr = 2

    def __init__(self):
        self.derive_instance_attr = 3
        super(Derive, self).__init__()


if __name__ == "__main__":
    ad = Derive()
    print(ad.derive_instance_attr)
    print(ad.derive_class_attr)
    print(ad.base_instance_attr)
    print(ad.base_class_attr)
