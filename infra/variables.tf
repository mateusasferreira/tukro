variable "aws_region" {
  type = string
}

variable "db_name" {
  type = string
}

variable "db_dialect" {
  type = string
}

variable "db_version" {
  type = string
}

variable "db_username" {
  type      = string
  sensitive = true
}

variable "db_password" {
  type      = string
  sensitive = true
}

variable "app_secret" {
  type = string
  sensitive = true
}

variable "jwt_secret" {
  type = string
  sensitive = true
}

variable "django_settings_module" {
  type = string
}

variable "key_pair_name" {
  type = string
}