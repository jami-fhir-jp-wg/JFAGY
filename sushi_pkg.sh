#!/bin/bash
\rm -rf ~/.fhir
cp -r ~/.fhir_sushiVersion ~/.fhir
sushi -s .
\rm -rf ~/.fhir
cp -r ~/.fhir.validation ~/.fhir
