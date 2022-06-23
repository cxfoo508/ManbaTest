function send_yaml(){	
	echo "发送yaml文件到服务！"
	password="a!3[[\DK6}*hRmHj86uCrE"
	path="/home/works/wulai-core/agents/my-agent/skills/faq"
	export PWD=$password 
	expect -c "
		spawn scp -r ./domain.yaml works@172.17.202.22:${path}
		expect "*password*"
		send \$env(PWD)\r
		interact"
}
`python ./tools/build_module.py`
send_yaml
