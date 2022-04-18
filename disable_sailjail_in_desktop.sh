#!/bin/bash

for desktopFile in $@; do
    if grep -q "^\[X-Sailjail\]" $desktopFile && ! grep -q "^Sandboxing=Disabled" $desktopFile; then
        echo "Disabling sailjail in: $desktopFile"
        sed -i '/^\[X-Sailjail\]/a Sandboxing=Disabled' $desktopFile || true
        # disabling sandboxing doesn't work if there is OrganizationName set
        sed -i 's|^OrganizationName|#OrganizationName|' $desktopFile || true
    fi
done

