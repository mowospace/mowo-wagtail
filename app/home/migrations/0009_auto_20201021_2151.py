# Generated by Django 3.0.10 on 2020-10-21 21:51

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201020_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('page_heading_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Section', label='Heading', max_length=80, required=False))])), ('hero_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Feature', label='Feature', max_length=80, required=False)), ('subheading', wagtail.core.blocks.CharBlock(default='Super Awesome Hero Subheading', label='Subheading', max_length=100, required=False)), ('description', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Description', max_length=400, required=False)), ('button', wagtail.core.blocks.CharBlock(default='Get in touch', label='Button text', max_length=100, required=False)), ('button_link', wagtail.core.blocks.URLBlock(label='Button link', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False))])), ('logo_cloud_block', wagtail.core.blocks.StructBlock([('logos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))])))])), ('service_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(label='Title', max_length=100, required=True)), ('services', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('logo', wagtail.core.blocks.RawHTMLBlock(required=True)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('description', wagtail.core.blocks.TextBlock(max_length=300, required=True))])))])), ('feature_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(label='Title', max_length=100, required=True)), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.RawHTMLBlock(required=True, rows=5)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('description', wagtail.core.blocks.TextBlock(max_length=300, required=True))])))])), ('counter_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(label='Title', max_length=100, required=True)), ('counters', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.TextBlock(max_length=300, required=True)), ('count', wagtail.core.blocks.IntegerBlock(max_value=1000000, required=True))])))])), ('cta_section_block', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('option-1', 'Option 1'), ('option-2', 'Option 2')])), ('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Product', label='Heading', max_length=80, required=False)), ('description', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Description', max_length=400, required=False)), ('button', wagtail.core.blocks.CharBlock(default='Get in touch', label='Button text', max_length=20, required=False)), ('button_link', wagtail.core.blocks.URLBlock(label='Button Link', required=False))])), ('pricing_section_block', wagtail.core.blocks.StructBlock([('custom_classes', wagtail.core.blocks.CharBlock(label='Classes', max_length=100, required=False)), ('heading', wagtail.core.blocks.CharBlock(label='Heading', max_length=100, required=False)), ('pricings', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('price', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('type', wagtail.core.blocks.ChoiceBlock(choices=[('monthly', 'Monthly'), ('unique', 'Unique')])), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('available', wagtail.core.blocks.BooleanBlock(required=False))])))])))])), ('content_section_block', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('centered', 'Centered'), ('two_columns_with_image', 'Two columns with image')])), ('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Section', label='Heading', max_length=80, required=False)), ('content', wagtail.core.blocks.RichTextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Content', max_length=10000, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('testimonial_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Feature', label='Feature', max_length=80, required=False)), ('subheading', wagtail.core.blocks.CharBlock(default='Super Awesome Hero Subheading', label='Subheading', max_length=100, required=False)), ('description', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Description', max_length=400, required=False)), ('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('category', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('content', wagtail.core.blocks.TextBlock(max_length=300, required=True))])))])), ('portfolio_section_block', wagtail.core.blocks.StructBlock([('custom_classes', wagtail.core.blocks.CharBlock(label='Classes', max_length=100, required=False)), ('heading', wagtail.core.blocks.CharBlock(label='Heading', max_length=100, required=False)), ('description', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Description', max_length=400, required=False)), ('projects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('description', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('link', wagtail.core.blocks.URLBlock(max_length=100, required=True))])))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subpage',
            name='content',
            field=wagtail.core.fields.StreamField([('page_heading_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Section', label='Heading', max_length=80, required=False))])), ('hero_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Feature', label='Feature', max_length=80, required=False)), ('subheading', wagtail.core.blocks.CharBlock(default='Super Awesome Hero Subheading', label='Subheading', max_length=100, required=False)), ('description', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Description', max_length=400, required=False)), ('button', wagtail.core.blocks.CharBlock(default='Get in touch', label='Button text', max_length=100, required=False)), ('button_link', wagtail.core.blocks.URLBlock(label='Button link', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False))])), ('logo_cloud_block', wagtail.core.blocks.StructBlock([('logos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))])))])), ('service_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(label='Title', max_length=100, required=True)), ('services', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('logo', wagtail.core.blocks.RawHTMLBlock(required=True)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('description', wagtail.core.blocks.TextBlock(max_length=300, required=True))])))])), ('feature_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(label='Title', max_length=100, required=True)), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.RawHTMLBlock(required=True, rows=5)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('description', wagtail.core.blocks.TextBlock(max_length=300, required=True))])))])), ('counter_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(label='Title', max_length=100, required=True)), ('counters', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.TextBlock(max_length=300, required=True)), ('count', wagtail.core.blocks.IntegerBlock(max_value=1000000, required=True))])))])), ('cta_section_block', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('option-1', 'Option 1'), ('option-2', 'Option 2')])), ('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Product', label='Heading', max_length=80, required=False)), ('description', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Description', max_length=400, required=False)), ('button', wagtail.core.blocks.CharBlock(default='Get in touch', label='Button text', max_length=20, required=False)), ('button_link', wagtail.core.blocks.URLBlock(label='Button Link', required=False))])), ('pricing_section_block', wagtail.core.blocks.StructBlock([('custom_classes', wagtail.core.blocks.CharBlock(label='Classes', max_length=100, required=False)), ('heading', wagtail.core.blocks.CharBlock(label='Heading', max_length=100, required=False)), ('pricings', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('price', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('type', wagtail.core.blocks.ChoiceBlock(choices=[('monthly', 'Monthly'), ('unique', 'Unique')])), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('available', wagtail.core.blocks.BooleanBlock(required=False))])))])))])), ('content_section_block', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('centered', 'Centered'), ('two_columns_with_image', 'Two columns with image')])), ('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Section', label='Heading', max_length=80, required=False)), ('content', wagtail.core.blocks.RichTextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Content', max_length=10000, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('testimonial_section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Super Awesome Feature', label='Feature', max_length=80, required=False)), ('subheading', wagtail.core.blocks.CharBlock(default='Super Awesome Hero Subheading', label='Subheading', max_length=100, required=False)), ('description', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Description', max_length=400, required=False)), ('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('category', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('content', wagtail.core.blocks.TextBlock(max_length=300, required=True))])))])), ('portfolio_section_block', wagtail.core.blocks.StructBlock([('custom_classes', wagtail.core.blocks.CharBlock(label='Classes', max_length=100, required=False)), ('heading', wagtail.core.blocks.CharBlock(label='Heading', max_length=100, required=False)), ('description', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Description', max_length=400, required=False)), ('projects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('description', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('link', wagtail.core.blocks.URLBlock(max_length=100, required=True))])))]))], blank=True, null=True),
        ),
    ]