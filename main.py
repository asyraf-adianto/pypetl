import pypetl as etl

etl.config.aws_enable()
etl.config.tunnel_enable()
etl.config.set_aws_secret('rds', 'renos-db-rds-staging-data')
etl.config.set_aws_secret('redshift', 'renos-wh-redshift-data')
etl.config.set_aws_secret('bastion', 'renos-data-bastion')
etl.engine.start()
etl.engine.stop()