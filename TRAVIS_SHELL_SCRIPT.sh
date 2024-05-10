#!/bin/bash

set -e

# Single Record Set

# Blue Route TRCVan2
main_dir="/home/croback_linux/s3bucket/Deployment_2_SEOhio/Blue Route/TRCVan2/"

export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1691072577/"
python getMetadataExp.py "1691072577" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691072577/20230803102431_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1691072577/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691072577/20230803102431_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1691075427/"
python getMetadataExp.py "1691075427" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691075427/20230803111216_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1691075427/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691075427/20230803111216_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1691081526/"
python getMetadataExp.py "1691081526" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691081526/20230803125408_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1691081526/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691081526/20230803125408_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1691084538/"
python getMetadataExp.py "1691084538" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691084538/20230803134341_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1691084538/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691084538/20230803134341_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1691087271/"
python getMetadataExp.py "1691087271" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691087271/20230803142920_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1691087271/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691087271/20230803142920_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1691504361/"
python getMetadataExp.py "1691504361" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691504361/20230808102628_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1691504361/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691504361/20230808102628_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1691508219/"
python getMetadataExp.py "1691508219" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691508219/20230808112603_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1691508219/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691508219/20230808112603_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1691511606/"
python getMetadataExp.py "1691511606" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691511606/20230808122312_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1691511606/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1691511606/20230808122312_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1692887823/"
python getMetadataExp.py "1692887823" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1692887823/20230824104552_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1692887823/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1692887823/20230824104552_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1692891046/"
python getMetadataExp.py "1692891046" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1692891046/20230824113426_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1692891046/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1692891046/20230824113426_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1692896526/"
python getMetadataExp.py "1692896526" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1692896526/20230824131233_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1692896526/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1692896526/20230824131233_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1692900817/"
python getMetadataExp.py "1692900817" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1692900817/20230824141453_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1692900817/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1692900817/20230824141453_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1697724037/"
python getMetadataExp.py "1697724037" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1697724037/20231019103308_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1697724037/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1697724037/20231019103308_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/Blue Route/1697730205/"
python getMetadataExp.py "1697730205" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/BlueRoute/1697730205/20231019114621_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/Blue\ Route/TRCVan2/1697730205/
rm /home/tmoleski_linux/metadataOverlayData/BlueRoute/1697730205/20231019114621_metadataVidMatched.avi
trash-empty

# Red Route TRCVan2
main_dir="/home/croback_linux/s3bucket/Deployment_2_SEOhio/RedRoute/TRCVan2/"

export_dir="/home/tmoleski_linux/metadataOverlayData/RedRoute/1691517970/"
python getMetadataExp.py "1691517970" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/RedRoute/1691517970/20230808141558_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/RedRoute/TRCVan2/1691517970/
rm /home/tmoleski_linux/metadataOverlayData/RedRoute/1691517970/20230808141558_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/RedRoute/1697559721/"
python getMetadataExp.py "1697559721" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/RedRoute/1697559721/20231017123635_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/RedRoute/TRCVan2/1697559721/
rm /home/tmoleski_linux/metadataOverlayData/RedRoute/1697559721/20231017123635_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/RedRoute/1697562875/"
python getMetadataExp.py "1697562875" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/RedRoute/1697562875/20231017131710_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/RedRoute/TRCVan2/1697562875/
rm /home/tmoleski_linux/metadataOverlayData/RedRoute/1697562875/20231017131710_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/RedRoute/1697569600/"
python getMetadataExp.py "1697569600" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/RedRoute/1697569600/20231017151026_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/RedRoute/TRCVan2/1697569600/
rm /home/tmoleski_linux/metadataOverlayData/RedRoute/1697569600/20231017151026_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/RedRoute/1697572375/"
python getMetadataExp.py "1697572375" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/RedRoute/1697572375/20231017155538_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/RedRoute/TRCVan2/1697572375/
rm /home/tmoleski_linux/metadataOverlayData/RedRoute/1697572375/20231017155538_metadataVidMatched.avi
trash-empty

# Green Route TRCVan2
main_dir="/home/croback_linux/s3bucket/Deployment_2_SEOhio/GreenRoute/TRCVan2/"

export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1691678548/"
python getMetadataExp.py "1691678548" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691678548/20230810104912_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1691678548/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691678548/20230810104912_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1691679859/"
python getMetadataExp.py "1691679859" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691679859/20230810110659_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1691679859/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691679859/20230810110659_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1691680851/"
python getMetadataExp.py "1691680851" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691680851/20230810112305_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1691680851/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691680851/20230810112305_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1691681779/"
python getMetadataExp.py "1691681779" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691681779/20230810113914_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1691681779/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691681779/20230810113914_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1691683677/"
python getMetadataExp.py "1691683677" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691683677/20230810121006_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1691683677/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691683677/20230810121006_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1691684637/"
python getMetadataExp.py "1691684637" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691684637/20230810122612_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1691684637/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1691684637/20230810122612_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1692718087/"
python getMetadataExp.py "1692718087" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692718087/20230822113405_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1692718087/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692718087/20230822113405_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1692720346/"
python getMetadataExp.py "1692720346" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692720346/20230822120757_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1692720346/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692720346/20230822120757_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1692721184/"
python getMetadataExp.py "1692721184" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692721184/20230822122108_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1692721184/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692721184/20230822122108_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1692722030/"
python getMetadataExp.py "1692722030" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692722030/20230822123743_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1692722030/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692722030/20230822123743_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1692723072/"
python getMetadataExp.py "1692723072" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692723072/20230822130021_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1692723072/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692723072/20230822130021_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1692724389/"
python getMetadataExp.py "1692724389" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692724389/20230822131909_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1692724389/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692724389/20230822131909_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1692725685/"
python getMetadataExp.py "1692725685" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692725685/20230822133724_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1692725685/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1692725685/20230822133724_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701070980/"
python getMetadataExp.py "1701070980" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701070980/20231128115252_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701070980/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701070980/20231128115252_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701192784/"
python getMetadataExp.py "1701192784" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701192784/20231128123411_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701192784/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701192784/20231128123411_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701194185/"
python getMetadataExp.py "1701194185" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701194185/20231128125800_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701194185/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701194185/20231128125800_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701195386/"
python getMetadataExp.py "1701195386" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701195386/20231128131916_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701195386/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701195386/20231128131916_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701196779/"
python getMetadataExp.py "1701196779" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701196779/20231128134136_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701196779/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701196779/20231128134136_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701198151/"
python getMetadataExp.py "1701198151" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701198151/20231128140454_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701198151/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701198151/20231128140454_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701199673/"
python getMetadataExp.py "1701199673" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701199673/20231128142921_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701199673/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701199673/20231128142921_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701203037/"
python getMetadataExp.py "1701203037" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701203037/20231128152559_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701203037/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701203037/20231128152559_metadataVidMatched.avi
trash-empty


export_dir="/home/tmoleski_linux/metadataOverlayData/GreenRoute/1701204159/"
python getMetadataExp.py "1701204159" "$main_dir" "$export_dir"
aws s3 cp /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701204159/20231128154451_metadataVidMatched.avi s3://dot-aws-driveohio-stage/Deployment_2_SEOhio/GreenRoute/TRCVan2/1701204159/
rm /home/tmoleski_linux/metadataOverlayData/GreenRoute/1701204159/20231128154451_metadataVidMatched.avi
trash-empty


